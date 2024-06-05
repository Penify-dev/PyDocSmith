"""Common methods for parsing."""
import enum
import textwrap
import typing as T

PARAM_KEYWORDS = {
    "param",
    "parameter",
    "arg",
    "argument",
    "attribute",
    "key",
    "keyword",
    "note",
}
RAISES_KEYWORDS = {"raises", "raise", "except", "exception"}
DEPRECATION_KEYWORDS = {"deprecation", "deprecated"}
RETURNS_KEYWORDS = {"return", "returns"}
YIELDS_KEYWORDS = {"yield", "yields"}
EXAMPLES_KEYWORDS = {"example", "examples"}
NOTES_KEYWORDS = {"note", "notes"}


class ParseError(RuntimeError):
    """Base class for all parsing related errors."""


class DocstringStyle(enum.Enum):
    """Docstring style."""

    REST = 1
    GOOGLE = 2
    NUMPYDOC = 3
    EPYDOC = 4
    AUTO = 255


class RenderingStyle(enum.Enum):
    """Rendering style when unparsing parsed docstrings."""

    COMPACT = 1
    CLEAN = 2
    EXPANDED = 3


class DocstringMeta:
    """Docstring meta information.

    Symbolizes lines in form of

        :param arg: description
        :raises ValueError: if something happens
    """

    def __init__(
        self, args: T.List[str], description: T.Optional[str]
    ) -> None:
        """Initialize self.

        :param args: list of arguments. The exact content of this variable is
            dependent on the kind of docstring; it's used to distinguish
            between custom docstring meta information items.
        :param description: associated docstring description.
        """
        self.args = args
        self.description = description
        self.arg_name = None


class DocstringParam(DocstringMeta):
    """DocstringMeta symbolizing :param metadata."""

    def __init__(
        self,
        args: T.List[str],
        description: T.Optional[str],
        arg_name: str,
        type_name: T.Optional[str],
        is_optional: T.Optional[bool],
        default: T.Optional[str],
    ) -> None:
        """Initialize self."""
        super().__init__(args, description)
        self.arg_name = arg_name
        self.type_name = type_name
        self.is_optional = is_optional
        self.default = default


class DocstringReturns(DocstringMeta):
    """DocstringMeta symbolizing :returns or :yields metadata."""

    def __init__(
        self,
        args: T.List[str],
        description: T.Optional[str],
        type_name: T.Optional[str],
        is_generator: bool,
        return_name: T.Optional[str] = None,
    ) -> None:
        """Initialize self."""
        super().__init__(args, description)
        self.type_name = type_name
        self.is_generator = is_generator
        self.return_name = return_name
        self.arg_name = None


class DocstringRaises(DocstringMeta):
    """DocstringMeta symbolizing :raises metadata."""

    def __init__(
        self,
        args: T.List[str],
        description: T.Optional[str],
        type_name: T.Optional[str],
    ) -> None:
        """Initialize self."""
        super().__init__(args, description)
        self.type_name = type_name
        self.description = description


class DocstringDeprecated(DocstringMeta):
    """DocstringMeta symbolizing deprecation metadata."""

    def __init__(
        self,
        args: T.List[str],
        description: T.Optional[str],
        version: T.Optional[str],
    ) -> None:
        """Initialize self."""
        super().__init__(args, description)
        self.version = version
        self.description = description


class DocstringExample(DocstringMeta):
    """DocstringMeta symbolizing example metadata."""

    def __init__(
        self,
        args: T.List[str],
        snippet: T.Optional[str],
        description: T.Optional[str],
    ) -> None:
        """Initialize self."""
        super().__init__(args, description)
        self.snippet = snippet
        self.description = description


class DocstringNote(DocstringMeta):
    """DocstringNote symbolizing example metadata."""

    def __init__(
        self,
        args: T.List[str],
        snippet: T.Optional[str],
        description: T.Optional[str],
    ) -> None:
        """Initialize self."""
        super().__init__(args, description)
        self.snippet = snippet
        self.description = description


class Docstring:
    """Docstring object representation."""

    def __init__(
        self,
        style=None,  # type: T.Optional[DocstringStyle]
    ) -> None:
        """Initialize self."""
        self.short_description = None  # type: T.Optional[str]
        self.long_description = None  # type: T.Optional[str]
        self.blank_after_short_description = False
        self.blank_after_long_description = False
        self.meta: T.List[DocstringMeta] = []  # type: T.List[DocstringMeta]
        self.style = style  # type: T.Optional[DocstringStyle]

    @property
    def params(self) -> T.List[DocstringParam]:
        """Return a list of information on function params."""
        return [item for item in self.meta if isinstance(item, DocstringParam)]

    @property
    def raises(self) -> T.List[DocstringRaises]:
        """Return a list of information on the exceptions that the function
        may raise.
        """
        return [
            item for item in self.meta if isinstance(item, DocstringRaises)
        ]

    @property
    def returns(self) -> T.Optional[DocstringReturns]:
        """Return a single information on function return.

        Takes the first return information.
        """
        for item in self.meta:
            if isinstance(item, DocstringReturns):
                return item
        return None

    @property
    def many_returns(self) -> T.List[DocstringReturns]:
        """Return a list of information on function return."""
        return [
            item for item in self.meta if isinstance(item, DocstringReturns)
        ]

    @property
    def deprecation(self) -> T.Optional[DocstringDeprecated]:
        """Return a single information on function deprecation notes."""
        for item in self.meta:
            if isinstance(item, DocstringDeprecated):
                return item
        return None

    @property
    def examples(self) -> T.List[DocstringExample]:
        """Return a list of information on function examples."""
        return [
            item for item in self.meta if isinstance(item, DocstringExample)
        ]

    @property
    def notes(self) -> T.List[DocstringNote]:
        """Return a list of information on function notes."""
        return [item for item in self.meta if isinstance(item, DocstringNote)]
    
def format_docstring_to_pep257(docstring: Docstring, width: int = 72) -> Docstring:
    if docstring.short_description:
        docstring.short_description = textwrap.fill(docstring.short_description.strip(), width)
    if docstring.long_description:
        docstring.long_description = textwrap.fill(docstring.long_description.strip(), width)

    for meta in docstring.meta:
        if meta.description:
            # Ensure meta descriptions are wrapped according to PEP 8
            split_description = meta.description.split("\n")
            for itm, idx in enumerate(split_description):
                split_description[idx] = textwrap.fill(itm.strip(), width)

            meta.description = "\n".join(split_description)
        if meta.args:
            # Clean up args to ensure they are stripped of extra spaces
            meta.args = [arg.strip() for arg in meta.args if arg.strip()]

    return docstring
    
