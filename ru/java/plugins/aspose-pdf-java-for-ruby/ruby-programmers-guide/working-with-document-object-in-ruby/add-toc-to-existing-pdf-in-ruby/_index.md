---
title: Добавить оглавление в существующий PDF в Ruby
type: docs
weight: 30
url: /ru/java/add-toc-to-existing-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Добавить оглавление

<ins>Чтобы добавить оглавление в PDF-документ, используя **Aspose.PDF Java для Ruby**, просто вызовите модуль **AddToc**.

Ruby Code

```java
# Путь к директории документов.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть PDF-документ.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Получить доступ к первой странице PDF-файла

toc_page = doc.getPages().insert(1)

# Создать объект для представления информации об оглавлении

toc_info = Rjb::import('com.aspose.pdf.TocInfo').new

title = Rjb::import('com.aspose.pdf.TextFragment').new("Table Of Contents")

title.getTextState().setFontSize(20)

#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# Установить заголовок для оглавления

toc_info.setTitle(title)

toc_page.setTocInfo(toc_info)

# Создать строковые объекты, которые будут использоваться как элементы оглавления

titles = Array["Первая страница", "Вторая страница"]

i = 0

while i < 2

    # Создать объект заголовка

    heading2 = Rjb::import('com.aspose.pdf.Heading').new(1)

    segment2 = Rjb::import('com.aspose.pdf.TextSegment').new

    heading2.setTocPage(toc_page)

    heading2.getSegments().add(segment2)

    # Указать страницу назначения для объекта заголовка

    heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

    # Страница назначения

    heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

    # Координата назначения

    segment2.setText(titles[i])

    # Добавить заголовок на страницу, содержащую оглавление

    toc_page.getParagraphs().add(heading2)

    i +=1

end

# Сохранить PDF-документ

doc.save(data_dir + "TOC.pdf")

puts "Оглавление добавлено успешно, пожалуйста, проверьте выходной файл."
```


## <ins> **Скачать Запущенный Код

Скачайте **Add TOC (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addtoc.rb)