यह प्रोजेक्ट मूल प्रोजेक्ट का एक फोर्क है - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith एक बहुमुखी Python पैकेज है जो विभिन्न शैलियों में docstrings को पार्स करने, पता लगाने और बनाने के लिए डिज़ाइन किया गया है। यह reStructuredText (reST), Google, NumPydoc, और Epydoc सहित कई docstring सम्मेलनों का समर्थन करता है, जो Python डेवलपर्स के लिए दस्तावेज़ीकरण प्रथाओं में लचीलापन प्रदान करता है।

## विशेषताएँ

- **Docstring शैली का पता लगाना:** सरल ह्यूरिस्टिक्स का उपयोग करके docstrings की शैली (जैसे, reST, Google, NumPydoc, Epydoc) को स्वचालित रूप से पता लगाता है।
- **Docstrings का पार्स करना:** docstrings को संरचित प्रतिनिधित्व में परिवर्तित करता है, जिससे दस्तावेज़ीकरण का विश्लेषण और हेरफेर करना आसान हो जाता है।
- **Docstrings का निर्माण:** संरचित docstrings को वापस टेक्स्ट में रेंडर करता है, जिससे स्वचालित docstring निर्माण और संशोधन की अनुमति मिलती है।
- **विशेषता Docstrings:** कक्षा और मॉड्यूल स्तर पर परिभाषित विशेषता docstrings को पार्स करता है, कक्षा गुणों और मॉड्यूल-स्तरीय चरों के दस्तावेज़ीकरण को बढ़ाता है।

## स्थापना

```bash
pip install PyDocSmith
```

## उपयोग

### Docstring शैली का पता लगाना

दिए गए टेक्स्ट की docstring शैली का पता लगाता है:

```python
from PyDocSmith import detect_docstring_style, DocstringStyle

docstring = """
यह एक उदाहरण docstring है।
:param param1: param1 का विवरण
:return: वापसी मूल्य का विवरण
"""
style = detect_docstring_style(docstring)
print(style)  # आउटपुट: DocstringStyle.EPYDOC
```

### Docstrings का पार्स करना

एक docstring को उसके घटकों में पार्स करता है:

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Docstrings का निर्माण

एक पार्स की गई docstring को वापस टेक्स्ट में रेंडर करता है:

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## उन्नत विशेषताएँ

- **ऑब्जेक्ट से पार्स करें:** PyDocSmith Python ऑब्जेक्ट्स से सीधे docstrings को पार्स कर सकता है, जिसमें कक्षाएं और मॉड्यूल शामिल हैं, संरचित प्रतिनिधित्व में विशेषता docstrings को शामिल करते हुए।
- **कस्टम रेंडरिंग शैलियाँ:** कॉम्पैक्ट या विस्तृत शैलियों के साथ docstrings का रेंडरिंग कस्टमाइज़ करें, और उत्पन्न docstring टेक्स्ट के लिए कस्टम इंडेंटेशन निर्दिष्ट करें।

## docstring_parser के संबंध में संशोधित चीजें

1. Docstring शैली का पता लगाने के लिए बेहतर ह्यूरिस्टिक्स
2. Google Docstring को Notes, Examples को समायोजित करने के लिए संशोधित किया गया
3. कभी-कभी GoogleDoc string में उचित इंडेंटेशन नहीं होता, विशेष रूप से जब LLMs जैसे GPT या Mistral से उत्पन्न होता है। PyDocSmith उन खराब docstrings को ठीक कर सकता है।
4. GoogleDocstring के विभिन्न शैली को समायोजित करने के लिए अतिरिक्त टेस्ट-केस जोड़े गए

मैंने इसे उपयोग के मामले के आधार पर अपडेट किया - https://www.penify.dev

## योगदान

योगदान स्वागत योग्य हैं! कृपया प्रोजेक्ट की GitHub पेज पर पुल रिक्वेस्ट सबमिट करें या मुद्दे रिपोर्ट करें।