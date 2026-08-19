---
title: Добавление JavaScript в Ruby
linktitle: Добавление JavaScript в Ruby
type: docs
weight: 10
url: /ru/java/adding-javascript-in-ruby/
description: Включите функциональность JavaScript в PDF с использованием Aspose.PDF в Ruby для интерактивности и автоматизации.
lastmod: "2026-08-19"
---
## Aspose.PDF – Добавление JavaScript

Чтобы добавить JavaScript в PDF‑документ с использованием **Aspose.PDF Java for Ruby**, просто вызовите модуль **AddJavaScript**.

Код Ruby

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

## Скачать работающий код

Скачать **Adding JavaScript (Aspose.PDF)** из любого из перечисленных ниже социальных кодовых сайтов:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)

