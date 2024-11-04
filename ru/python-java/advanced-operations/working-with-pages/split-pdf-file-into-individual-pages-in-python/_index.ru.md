---
title: Разделение PDF файла на отдельные страницы на Python
type: docs
weight: 80
url: /python-java/split-pdf-file-into-individual-pages-in-python/
---

<ins>Чтобы разделить PDF документ на отдельные страницы с помощью **Aspose.PDF Java for PHP**, просто вызовите класс **SplitAllPages**.

**Python Код**
```

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# перебираем все страницы
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# создаем новый объект Document
new_document = self.Document();

# получаем страницу по определенному индексу из коллекции страниц
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# сохраняем вновь созданный PDF файл
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "Процесс разделения успешно завершен!";
```

**Скачать выполняемый код**

Скачайте **Разделенные страницы (Aspose.PDF)** с любого из нижеупомянутых сайтов для совместной разработки:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/SplitAllPages/SplitAllPages.py)