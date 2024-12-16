---
title: تقسيم ملف PDF إلى صفحات فردية في روبي
type: docs
weight: 80
url: /ar/java/split-pdf-file-into-individual-pages-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - تقسيم الصفحات

لتقسيم مستند PDF إلى صفحات فردية باستخدام **Aspose.PDF Java for Ruby**، قم ببساطة باستدعاء وحدة **SplitAllPages**.

كود روبي

```java

# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح المستند الهدف

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# حلقة عبر جميع الصفحات

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# إنشاء كائن مستند جديد

new_document = Rjb::import('com.aspose.pdf.Document').new

# الحصول على الصفحة في فهرس معين من مجموعة الصفحات

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# حفظ ملف PDF الذي تم إنشاؤه حديثًا

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "تم إكمال عملية التقسيم بنجاح!"
```


## تنزيل الكود الجاري

قم بتنزيل **تقسيم الصفحات (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)