---
title: Получить XMP Метаданные из PDF файла на Python
type: docs
weight: 50
url: /ru/python-java/get-xmp-metadata-from-pdf-file-in-python/
---

<ins>Чтобы получить XMP метаданные из PDF документа, используя **Aspose.PDF Java для Python**, просто вызовите класс **GetXMPMetadata**.

**Код на Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Получить свойства
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**Скачать Запущенный Код**

Скачать **Получить XMP Метаданные (Aspose.PDF)** с любого из нижеупомянутых социальных сайтов кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)