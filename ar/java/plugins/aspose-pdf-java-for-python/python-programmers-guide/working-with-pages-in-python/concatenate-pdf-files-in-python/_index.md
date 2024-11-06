---
title: دمج ملفات PDF في بايثون
type: docs
weight: 10
url: ar/java/concatenate-pdf-files-in-python/
lastmod: "2021-06-05"
---

لدمج ملفات PDF باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء فئة **ConcatenatePdfFiles**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# افتح المستند المصدر
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# أضف صفحات المستند المصدر إلى المستند الهدف
pdf1.getPages().add(pdf1.getPages())

# احفظ ملف الإخراج المدمج (المستند الهدف)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "تم حفظ المستند الجديد، يرجى التحقق من ملف الإخراج"
```

**تحميل الشيفرة الجارية**

قم بتنزيل **دمج ملفات PDF (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)