---
title: Working with Headings in PDF
type: docs
weight: 90
url: /cpp/working-with-headings/
lastmod: "2021-11-11"
description: Create numbering in heading your PDF document with C++. Aspose.PDF for C++ shows different kinds of numbering styles.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Apply Numbering Style in Heading

Any text in a document begins with a heading. The headings are an integral part of the content, regardless of style and theme.
Headings help draw attention to the text and help users find the information they need in the document, improving readability and visual perception. Using heading styles, you can also quickly create a table of contents, change the structure of the document.
So, let's check out how to work with headers using the Aspose.PDF for C++ library.

[Aspose.PDF for C++](/pdf/cpp/) offers many pre-defined numbering styles. These pre-defined numbering styles are stored in an enumeration, NumberingStyle. The pre-defined values of NumberingStyle enumeration and their descriptions are given below:

|**Heading Types**|**Description**|
| :- | :- |
|NumeralsArabic|Arab type,for example, 1,1.1,...|
|NumeralsRomanUppercase|Roman upper type, for example, I,I.II, ...|
|NumeralsRomanLowercase|Roman lower type, for example, i,i.ii, ...|
|LettersUppercase|English upper type, for example, A,A.B, ...|
|LettersLowercase|English lower type, for example, a,a.b, ...|
The **Style** property of **Aspose.PDF.Heading** class is used to set the numbering styles of the headings.

|**Figure: Pre-defined numbering styles**|
| :- |
The source code, to obtain the output shown in the above figure, is given below in the example.

```cpp
void WorkingWithHeadingsInPDF() {
 // String for path name
 String _dataDir("C:\\Samples\\");

 // String for input file name
 String outputFileName("ApplyNumberStyle_out.pdf");

 // Open document
 auto document = MakeObject<Document>();

 document->get_PageInfo()->set_Width(612.0);
 document->get_PageInfo()->set_Height(792.0);
 document->get_PageInfo()->set_Margin (MakeObject<MarginInfo>());
 document->get_PageInfo()->get_Margin()->set_Left(72);
 document->get_PageInfo()->get_Margin()->set_Right(72);
 document->get_PageInfo()->get_Margin()->set_Top (72);
 document->get_PageInfo()->get_Margin()->set_Bottom (72);
        
 auto pdfPage = document->get_Pages()->Add();
 pdfPage->get_PageInfo()->set_Width (612.0);
 pdfPage->get_PageInfo()->set_Height (792.0);
 pdfPage->get_PageInfo()->set_Margin(MakeObject<MarginInfo>());
 pdfPage->get_PageInfo()->get_Margin()->set_Left(72);
 pdfPage->get_PageInfo()->get_Margin()->set_Right(72);
 pdfPage->get_PageInfo()->get_Margin()->set_Top(72);
 pdfPage->get_PageInfo()->get_Margin()->set_Bottom(72);

 auto floatBox = MakeObject<FloatingBox>();
 floatBox->set_Margin(pdfPage->get_PageInfo()->get_Margin());

 pdfPage->get_Paragraphs()->Add(floatBox);

 auto textFragment = MakeObject<TextFragment>();
 auto segment = MakeObject<TextSegment>();

 auto heading = MakeObject<Heading>(1);
 heading->set_IsInList(true);
 heading->set_StartNumber(1);
 heading->set_Text (u"List 1");
 heading->set_Style(NumberingStyle::NumeralsRomanLowercase);
 heading->set_IsAutoSequence(true);

 floatBox->get_Paragraphs()->Add(heading);

 auto heading2 = MakeObject<Heading>(1);
 heading2->set_IsInList (true);
 heading2->set_StartNumber(13);
 heading2->set_Text (u"List 2");
 heading2->set_Style(NumberingStyle::NumeralsRomanLowercase);
 heading2->set_IsAutoSequence(true);;

 floatBox->get_Paragraphs()->Add(heading2);

 auto heading3 = MakeObject<Heading>(2);
 heading3->set_IsInList (true);
 heading3->set_StartNumber(1);
 heading3->set_Text (u"the value, as of the effective date of the plan, of property to be distributed under the plan onaccount of each allowed");
 heading3->set_Style(NumberingStyle::LettersLowercase);
 heading3->set_IsAutoSequence(true);

 floatBox->get_Paragraphs()->Add(heading3); 

 // Save concatenated output file
 document->Save(_dataDir + outputFileName);
}
```
