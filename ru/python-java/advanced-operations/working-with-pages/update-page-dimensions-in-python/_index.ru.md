---
title: Обновление размеров страницы в Python
type: docs
weight: 90
url: /python-java/update-page-dimensions-in-python/
---

<ins>Чтобы обновить размеры страницы с помощью **Aspose.PDF Java для Python**, просто вызовите класс **UpdatePageDimensions**.

**Код на Python**
```s
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# получить коллекцию страниц
page_collection = pdf.getPages()

# получить определенную страницу
pdf_page = page_collection.get_Item(1)

# установить размер страницы как A4 (11.7 x 8.3 дюймов) и в Aspose.PDF, 1 дюйм = 72 точки
# поэтому размеры A4 в точках будут (842.4, 597.6)
pdf_page.setPageSize(597.6,842.4)

# сохранить вновь созданный PDF файл
pdf.save(self.dataDir + "output.pdf")

print "Размеры успешно обновлены!"

```

**Скачать выполняемый код**

Скачайте **Update Page Dimensions (Aspose.PDF)** с любого из нижеупомянутых сайтов для совместной разработки:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)
 - [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)