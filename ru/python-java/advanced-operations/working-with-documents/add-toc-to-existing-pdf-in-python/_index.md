---
title: Добавление содержания в существующий PDF на Python
type: docs
weight: 20
url: /ru/python-java/add-toc-to-existing-pdf-in-python/
---

Чтобы добавить содержание в PDF документ, используя **Aspose.PDF Java для Python**, просто вызовите класс **AddToc**.

```python

# Открыть PDF документ.
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Получить доступ к первой странице PDF файла
toc_page = doc.getPages().insert(1)

# Создать объект для представления информации о содержании
toc_info = self.TocInfo()
title = self.TextFragment("Содержание")
title.getTextState().setFontSize(20)

# Установить заголовок для содержания
toc_info.setTitle(title)
toc_page.setTocInfo(toc_info)

# Создать строковые объекты, которые будут использоваться как элементы содержания
titles = ["Первая страница", "Вторая страница"]

i = 0;
while (i < 2):

# Создать объект заголовка
heading2 = self.Heading(1)

segment2 = self.TextSegment
heading2.setTocPage(toc_page)
heading2.getSegments().add(segment2)

# Указать целевую страницу для объекта заголовка
heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

# Целевая страница
heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

# Целевая координата
segment2.setText(titles[i])

# Добавить заголовок на страницу, содержащую содержание
toc_page.getParagraphs().add(heading2)

i +=1

# Сохранить PDF документ
doc.save(self.dataDir + "TOC.pdf")

print "Содержание успешно добавлено, пожалуйста, проверьте выходной файл."
```


**Скачать Исполняемый Код**

Скачать **Add TOC (Aspose.PDF)** с любого из нижеупомянутых социальных сайтов с исходным кодом:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)