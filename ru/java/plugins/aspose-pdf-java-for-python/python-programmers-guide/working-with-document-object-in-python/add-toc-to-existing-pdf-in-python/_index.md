---
title: Добавить оглавление в существующий PDF на Python
type: docs
weight: 20
url: /ru/java/add-toc-to-existing-pdf-in-python/
lastmod: "2021-06-05"
---

Чтобы добавить оглавление в PDF-документ с использованием **Aspose.PDF Java для Python**, просто вызовите класс **AddToc**.

```python

# Открыть PDF-документ.
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Получить доступ к первой странице PDF-файла
toc_page = doc.getPages().insert(1)

# Создать объект для представления информации об оглавлении
toc_info = self.TocInfo()
title = self.TextFragment("Содержание")
title.getTextState().setFontSize(20)

# Установить заголовок для оглавления
toc_info.setTitle(title)
toc_page.setTocInfo(toc_info)

# Создать строковые объекты, которые будут использоваться как элементы оглавления
titles = ["Первая страница", "Вторая страница"]

i = 0;
while (i < 2):

# Создать объект заголовка
heading2 = self.Heading(1);

segment2 = self.TextSegment
heading2.setTocPage(toc_page)
heading2.getSegments().add(segment2)

# Указать целевую страницу для объекта заголовка
heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

# Целевая страница
heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

# Координата назначения
segment2.setText(titles[i])

# Добавить заголовок на страницу, содержащую оглавление
toc_page.getParagraphs().add(heading2)

i +=1;

# Сохранить PDF-документ
doc.save(self.dataDir + "TOC.pdf")

print "Оглавление добавлено успешно, пожалуйста, проверьте выходной файл."
```
```


**Скачать Исполняемый Код**

Скачайте **Add TOC (Aspose.PDF)** с любого из указанных ниже социальных сайтов для разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)