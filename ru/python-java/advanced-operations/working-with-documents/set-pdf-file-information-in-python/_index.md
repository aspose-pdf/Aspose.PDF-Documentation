---
title: Установить информацию о PDF файле на Python
type: docs
weight: 90
url: ru/python-java/set-pdf-file-information-in-python/
---

<ins>Чтобы обновить информацию о Pdf документе с использованием **Aspose.PDF Java for Python**, просто вызовите класс **SetPdfFileInfo**.

**Python Code**
```
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Получить информацию о документе
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF for java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("Информация о PDF");
doc_info.setTitle("Установка информации о PDF документе");

# сохранить обновленный документ с новой информацией

doc.save(self.dataDir + "Updated_Information.pdf")
print "Информация о документе обновлена, пожалуйста, проверьте выходной файл."
```

**Скачать запускаемый код**

Скачайте **Установить информацию о PDF файле (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)