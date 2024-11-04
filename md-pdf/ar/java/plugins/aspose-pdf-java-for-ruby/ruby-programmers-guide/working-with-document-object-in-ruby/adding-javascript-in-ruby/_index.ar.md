---
title: إضافة JavaScript في روبي
type: docs
weight: 10
url: /java/adding-javascript-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - إضافة JavaScript

لإضافة JavaScript في مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، ببساطة نفذ وحدة **AddJavaScript**.

كود روبي

```java
# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح مستند pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# إضافة JavaScript على مستوى المستند

# إنشاء JavascriptAction مع عبارة JavaScript المطلوبة

javaScript = Rjb::import('com.aspose.pdf.JavascriptAction').new("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# تعيين كائن JavascriptAction إلى الإجراء المطلوب للمستند

doc.setOpenAction(javaScript)

# إضافة JavaScript على مستوى الصفحة

doc.getPages().get_Item(2).getActions().setOnOpen(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is opened')"))

doc.getPages().get_Item(2).getActions().setOnClose(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is closed')"))

# حفظ مستند PDF

doc.save(data_dir + "JavaScript-Added.pdf")

puts "تمت إضافة JavaScript بنجاح، يرجى التحقق من ملف الإخراج."
```


## تنزيل الكود الجاري

قم بتنزيل **إضافة JavaScript (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)