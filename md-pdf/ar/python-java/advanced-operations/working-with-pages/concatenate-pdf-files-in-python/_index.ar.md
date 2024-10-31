---
title: دمج ملفات PDF في بايثون
type: docs
weight: 10
url: /python-java/concatenate-pdf-files-in-python/
---

لدمج ملفات PDF باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء فئة **ConcatenatePdfFiles**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# افتح مستند المصدر
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# أضف صفحات مستند المصدر إلى المستند الهدف
pdf1.getPages().add(pdf1.getPages())

# احفظ الملف الناتج المدمج (المستند الهدف)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "تم حفظ المستند الجديد، يرجى التحقق من ملف الإخراج"
```

**تحميل الكود التشغيلي**

قم بتحميل **دمج ملفات PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)