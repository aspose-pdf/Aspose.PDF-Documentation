---
title: تحويل صفحات PDF إلى صور في روبي
type: docs
weight: 20
url: ar/java/convert-pdf-pages-to-images-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - تحويل صفحات PDF إلى صور

لتحويل جميع الصفحات إلى صور من مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء وحدة **ConvertPagesToImages**.

كود روبي

```java

# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

    converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

    image_count +=1

end

puts "تم تحويل صفحات PDF إلى صور فردية بنجاح!"
```

## تحميل الكود التشغيلي

قم بتحميل **تحويل صفحات PDF إلى صور (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)

```ruby
# تحويل صفحات PDF إلى صور
require 'java'
require 'asposepdfjava'

java_import 'com.aspose.pdf.Document'
java_import 'com.aspose.pdf.devices.Resolution'
java_import 'com.aspose.pdf.devices.JpegDevice'

def convert_pages_to_images(input_pdf, output_path)
  # تحميل ملف PDF
  pdf_document = Document.new(input_pdf)

  # تعيين الدقة للصور
  resolution = Resolution.new(300)

  # تكرار من خلال الصفحات
  (1..pdf_document.pages.size).each do |page_number|
    # اختر الصفحة الحالية
    pdf_page = pdf_document.pages.get_Item(page_number)

    # إعداد جهاز الصورة
    jpeg_device = JpegDevice.new(resolution)

    # تحويل الصفحة إلى صورة وحفظها
    output_file = File.join(output_path, "page_#{page_number}.jpg")
    jpeg_device.process(pdf_page, output_file)
  end
end

# استدعاء الوظيفة مع مسار ملف PDF ومسار المجلد لحفظ الصور
convert_pages_to_images('sample.pdf', 'output_images')
```

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)