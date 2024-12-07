---
title: Insert an Empty Page at End of PDF File in Ruby
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
description: Discover how to insert an empty page at the end of a PDF document using Ruby with Aspose.PDF, adding flexibility to your PDF processing tasks.
lastmod: "2021-06-05"
---

## Aspose.PDF - Insert an Empty Page at End of PDF File

To Insert an Empty Page at the end of PDF document using **Aspose.PDF Java for Ruby**, simply invoke **InsertEmptyPageAtEndOfFile** module.

Ruby Code

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().add()

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## Download Running Code

Download **Insert an Empty Page at End of PDF File (Aspose.PDF)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)
