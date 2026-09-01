---
title: Définir l'expiration du PDF dans Ruby
linktitle: Définir l'expiration du PDF dans Ruby
type: docs
weight: 110
url: /java/set-pdf-expiration-in-ruby/
description: Implémentez les dates d'expiration dans les PDF à l'aide d'Aspose.PDF for Ruby pour les documents urgents.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Définir l'expiration du PDF



Pour définir l'expiration d'un document PDF à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **SetExpiration**.

Code Rubis


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

## 
Télécharger le code d'exécution



Téléchargez** Définir l'expiration du PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)
