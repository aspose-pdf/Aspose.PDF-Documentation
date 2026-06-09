---
title: Set PDF Expiration in Ruby
linktitle: Set PDF Expiration in Ruby
type: docs
weight: 110
url: /java/set-pdf-expiration-in-ruby/
description: Implement expiration dates in PDFs using Aspose.PDF for Ruby for time-sensitive documents.
lastmod: "2026-06-09"
---

## Aspose.PDF - Set PDF Expiration

To set expiration ofВ  Pdf document using **Aspose.PDF Java for Ruby**, simply invoke **SetExpiration** module.

Ruby Code

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

В В В  "var year=2014;

В В В  var month=4;

В В В  today = new Date();

В В В  today = new Date(today.getFullYear(), today.getMonth());

В В В  expiry = new Date(year, month);

В В В  if (today.getTime() > expiry.getTime())

В В В  app.alert('The file is expired. You need a new one.');")

doc.setOpenAction(javascript)

# save update document with new information

doc.save(data_dir + "set_expiration.pdf")

puts "Update document information, please check output file."
```

## Download Running Code

DownloadВ **Set PDF Expiration (Aspose.PDF)**В fromВ any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)
