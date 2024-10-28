---
title: Добавление JavaScript в Ruby
type: docs
weight: 10
url: /java/adding-javascript-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Добавление JavaScript

Чтобы добавить JavaScript в документ PDF с использованием **Aspose.PDF Java для Ruby**, просто вызовите модуль **AddJavaScript**.

Ruby Код

```java
# Путь к директории документов.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть PDF документ.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Добавление JavaScript на уровне документа

# Создание экземпляра JavascriptAction с желаемым JavaScript выражением

javaScript = Rjb::import('com.aspose.pdf.JavascriptAction').new("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Назначение объекта JavascriptAction желаемому действию документа

doc.setOpenAction(javaScript)

# Добавление JavaScript на уровне страницы

doc.getPages().get_Item(2).getActions().setOnOpen(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('страница 2 открыта')"))

doc.getPages().get_Item(2).getActions().setOnClose(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('страница 2 закрыта')"))

# Сохранение PDF документа

doc.save(data_dir + "JavaScript-Added.pdf")

puts "JavaScript успешно добавлен, пожалуйста, проверьте выходной файл."
```


## Загрузка выполняемого кода

Скачайте **Adding JavaScript (Aspose.PDF)** с любого из нижеупомянутых сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)