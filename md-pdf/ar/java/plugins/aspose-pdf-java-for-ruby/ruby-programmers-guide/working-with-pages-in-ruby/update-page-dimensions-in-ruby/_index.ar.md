---
title: تحديث أبعاد الصفحة في روبي
type: docs
weight: 90
url: /java/update-page-dimensions-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - تحديث أبعاد الصفحة

لتحديث أبعاد الصفحة باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء وحدة **UpdatePageDimensions**.

كود روبي

```java

# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح المستند الهدف

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# احصل على مجموعة الصفحات

page_collection = pdf.getPages()

# احصل على صفحة معينة

pdf_page = page_collection.get_Item(1)

# قم بتعيين حجم الصفحة إلى A4 (11.7 x 8.3 بوصة) وفي Aspose.PDF، 1 بوصة = 72 نقطة

# لذلك ستكون أبعاد A4 بالنقاط (842.4, 597.6)

pdf_page.setPageSize(597.6,842.4)

# احفظ ملف PDF الجديد الذي تم إنشاؤه

pdf.save(data_dir + "output.pdf")

puts "تم تحديث الأبعاد بنجاح!"
```

## تحميل الكود التشغيلي

قم بتحميل **تحديث أبعاد الصفحة (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)

```ruby
# تحميل مكتبة Aspose.PDF لـ Java
require 'asposepdfjava'

include Asposepdfjava

module UpdatePageDimensions
  def self.run()
    # المسار إلى دليل المستندات.
    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # فتح ملف PDF
    pdf_document = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'UpdatePageDimensions.pdf')

    # تعيين أبعاد الصفحة
    page = pdf_document.getPages().get_Item(1)
    page.setPageSize(500, 700)

    # حفظ الملف المحدث
    pdf_document.save(data_dir + 'UpdatePageDimensions_out.pdf')
  end
end
```

```yaml
changefreq: "monthly"
type: docs
`