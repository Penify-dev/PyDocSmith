यह परियोजना मूल परियोजना से एक फोर्क है - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith एक बहुमुखी Python पैकेज है जिसे विभिन्न शैलियों में डॉकस्ट्रिंग को पार्स करने, पता लगाने और लिखने के लिए डिज़ाइन किया गया है। यह reStructuredText (reST), Google, NumPydoc, और Epydoc सहित कई डॉकस्ट्रिंग सम्मेलनों का समर्थन करता है, जो Python डेवलपर्स के लिए दस्तावेजीकरण प्रथाओं में लचीलापन प्रदान करता है।

## विशेषताएं

- **डॉकस्ट्रिंग शैली का पता लगाना:** सरल ह्यूरिस्टिक्स का उपयोग करके डॉकस्ट्रिंग की शैली (जैसे, reST, Google, NumPydoc, Epydoc) को स्वचालित रूप से पता लगाएं।
- **डॉकस्ट्रिंग पार्सिंग:** डॉकस्ट्रिंग को संरचित प्रतिनिधित्व में परिवर्तित करें, जिससे दस्तावेजीकरण का विश्लेषण और हेरफेर करना आसान हो जाए।
- **डॉकस्ट्रिंग कम्पोज़िशन:** संरचित डॉकस्ट्रिंग को वापस टेक्स्ट में रेंडर करें, जिससे स्वचालित डॉकस्ट्रिंग जनरेशन और संशोधन की अनुमति मिले।
- **एट्रिब्यूट डॉकस्ट्रिंग:** क्लास और मॉड्यूल स्तर पर परिभाषित एट्रिब्यूट डॉकस्ट्रिंग को पार्स करें, क्लास प्रॉपर्टीज और मॉड्यूल-स्तरीय वेरिएबल्स के दस्तावेजीकरण को बढ़ाएं।

## इंस्टॉलेशन

```bash
pip install PyDocSmith
```

## उपयोग

### डॉकस्ट्रिंग शैली का पता लगाना

दिए गए टेक्स्ट की डॉकस्ट्रिंग शैली का पता लगाएं:

```python
from PyDocSmith import detect_docstring_style, DocstringStyle

docstring = """
This is an example docstring.
:param param1: Description of param1
:return: Description of return value
"""
style = detect_docstring_style(docstring)
print(style)  # Outputs: DocstringStyle.EPYDOC
```

### डॉकस्ट्रिंग पार्स करना

एक डॉकस्ट्रिंग को उसके घटकों में पार्स करें:

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### डॉकस्ट्रिंग कम्पोज़ करना

एक पार्स किए गए डॉकस्ट्रिंग को वापस टेक्स्ट में रेंडर करें:

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## अधिक उदाहरण

### NumPy शैली Docstrings का पार्सिंग

NumPy-शैली docstring को पार्स करें:

```python
from PyDocSmith import parse, DocstringStyle

docstring = """
Short description

Long description

Parameters
----------
param1 : int
    Description of param1
param2 : str, optional
    Description of param2

Returns
-------
int
    Description of return value
"""

parsed = parse(docstring, style=DocstringStyle.NUMPYDOC)
print(parsed)
```

### Python ऑब्जेक्ट्स से पार्सिंग

Python कार्यों या कक्षाओं से सीधे docstrings को पार्स करें:

```python
from PyDocSmith import parse_from_object

def example_function(param1: int, param2: str = "default") -> int:
    """
    This is an example function.

    Args:
        param1 (int): First parameter
        param2 (str): Second parameter

    Returns:
        int: The result
    """
    return param1 + len(param2)

parsed = parse_from_object(example_function)
print(parsed)
```

### विभिन्न शैलियों के साथ कम्पोज़िंग

विश्लेषित किए गए शैली से अलग शैली में docstring को कम्पोज़ करें:

```python
from PyDocSmith import compose, DocstringStyle

# Assuming you have a parsed_docstring from previous examples
docstring_text = compose(parsed_docstring, style=DocstringStyle.GOOGLE)
print(docstring_text)
```

## उन्नत विशेषताएं

- **ऑब्जेक्ट से पार्स करें:** PyDocSmith Python ऑब्जेक्ट्स से सीधे डॉकस्ट्रिंग पार्स कर सकता है, जिसमें क्लासेस और मॉड्यूल्स शामिल हैं, एट्रिब्यूट डॉकस्ट्रिंग को संरचित प्रतिनिधित्व में शामिल करते हुए।
- **कस्टम रेंडरिंग शैलियां:** कॉम्पैक्ट या डिटेल्ड शैलियों के साथ डॉकस्ट्रिंग के रेंडरिंग को कस्टमाइज़ करें, और जनरेट किए गए डॉकस्ट्रिंग टेक्स्ट के लिए कस्टम इंडेंटेशन निर्दिष्ट करें।


