---
title: إضافة JavaScript في Ruby
linktitle: إضافة JavaScript في Ruby
type: docs
weight: 10
url: /ar/java/adding-javascript-in-ruby/
description: تمكين وظيفة JavaScript في ملفات PDF باستخدام Aspose.PDF في Ruby للتفاعل والأتمتة.
lastmod: "2026-10-01"
---
## Aspose.PDF - إضافة JavaScript

لإضافة JavaScript في مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء الوحدة **AddJavaScript**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Adding JavaScript at Document Level

# Instantiate JavascriptAction with desried JavaScript statement

javaScript = Rjb::import('com.aspose.pdf.JavascriptAction').new("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Assign JavascriptAction object to desired action of Document

doc.setOpenAction(javaScript)

# Adding JavaScript at Page Level

doc.getPages().get_Item(2).getActions().setOnOpen(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is opened')"))

doc.getPages().get_Item(2).getActions().setOnClose(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is closed')"))

# Save PDF Document

doc.save(data_dir + "JavaScript-Added.pdf")

puts "Added JavaScript Successfully, please check the output file."
```

## تنزيل الكود التشغيلي

تنزيل **إضافة JavaScript (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)
