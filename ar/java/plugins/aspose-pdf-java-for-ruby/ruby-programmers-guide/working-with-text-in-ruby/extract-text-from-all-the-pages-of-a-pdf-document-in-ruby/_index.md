---
title: استخراج النص من جميع صفحات وثيقة PDF في روبي
linktitle: استخراج النص من جميع صفحات وثيقة PDF في روبي
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
description: افهم كيفية استخراج النص من جميع صفحات مستند PDF باستخدام Ruby وAspose.PDF، وهو مثالي لتحليل المحتوى.
lastmod: "2026-06-09"
---
## Aspose.PDF - استخراج النص من كافة الصفحات

لاستخراج TextrFrom All Pages Pdf باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **ExtractTextFromAllPages**.

كود روبي

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

## تحميل كود التشغيل

تنزيلВ **استخراج النص من جميع الصفحات (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)
