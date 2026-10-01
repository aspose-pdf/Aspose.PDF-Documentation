---
title: استخراج النص من جميع صفحات مستند PDF في Ruby
linktitle: استخراج النص من جميع صفحات مستند PDF في Ruby
type: docs
weight: 30
url: /ar/java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
description: تعرف على كيفية استخراج النص من جميع صفحات مستند PDF باستخدام Ruby و Aspose.PDF، وهو مثالي لتحليل المحتوى.
lastmod: "2026-10-01"
---
## Aspose.PDF - استخراج النص من جميع الصفحات

لاستخراج TextrFrom جميع صفحات مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، قم ببساطة باستدعاء وحدة **ExtractTextFromAllPages**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# create TextAbsorber object to extract text

text_absorber = Rjb::import('com.aspose.pdf.TextAbsorber').new

# accept the absorber for all the pages

pdf.getPages().accept(text_absorber)

# In order to extract text from specific page of document, we need to specify the particular page using its index against accept(..) method.

# accept the absorber for particular PDF page

# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

#get the extracted text

extracted_text = text_absorber.getText()

# create a writer and open the file

writer = Rjb::import('java.io.FileWriter').new(Rjb::import('java.io.File').new(data_dir + "extracted_text.out.txt"))

writer.write(extracted_text)

# write a line of text to the file

# tw.WriteLine(extractedText);

# close the stream

writer.close()

puts "Text extracted successfully. Check output file."
```

## تنزيل الكود الجاري

تحميلВ **استخراج النص من جميع الصفحات (Aspose.PDF)**В منВ أي من المواقع الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)
