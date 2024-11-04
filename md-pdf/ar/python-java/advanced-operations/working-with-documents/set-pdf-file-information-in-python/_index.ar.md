---
title: ضبط معلومات ملف PDF في بايثون
type: docs
weight: 90
url: /python-java/set-pdf-file-information-in-python/
---

<ins>لتحديث معلومات مستند Pdf باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء فئة **SetPdfFileInfo**.

**كود بايثون**
```
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# الحصول على معلومات المستند
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF for java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("معلومات PDF");
doc_info.setTitle("ضبط معلومات مستند PDF");

# حفظ المستند المحدث بالمعلومات الجديدة

doc.save(self.dataDir + "Updated_Information.pdf")
print "تم تحديث معلومات المستند، يرجى التحقق من ملف الإخراج."
```

**تنزيل الكود القابل للتشغيل**

قم بتنزيل **ضبط معلومات ملف PDF (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)