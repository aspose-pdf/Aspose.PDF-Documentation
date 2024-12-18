---
title: تعيين معلومات ملف PDF في بايثون
type: docs
weight: 90
url: /ar/java/set-pdf-file-information-in-python/
lastmod: "2021-06-05"
---

لتحديث معلومات مستند Pdf باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء فئة **SetPdfFileInfo**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# الحصول على معلومات المستند
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF for java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("PDF Information");
doc_info.setTitle("Setting PDF Document Information");

# حفظ المستند المحدث بالمعلومات الجديدة

doc.save(self.dataDir + "Updated_Information.pdf")
print "Update document information, please check output file."
```

**تنزيل الكود التنفيذي**

قم بتنزيل **تعيين معلومات ملف PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)