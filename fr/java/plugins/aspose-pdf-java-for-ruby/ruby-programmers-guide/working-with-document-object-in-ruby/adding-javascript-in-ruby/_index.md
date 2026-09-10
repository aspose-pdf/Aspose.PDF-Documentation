---
title: Ajout de JavaScript dans Ruby
linktitle: Ajout de JavaScript dans Ruby
type: docs
weight: 10
url: /java/adding-javascript-in-ruby/
description: Activez la fonctionnalité JavaScript dans les PDF à l'aide d'Aspose.PDF dans Ruby pour l'interactivité et l'automatisation.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Ajout de JavaScript



Pour ajouter du JavaScript dans un document PDF à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **AddJavaScript**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Adding JavaScript at Document Level

# Instantiate JavascriptAction with desried JavaScript statement

javaScript = Rjb::import('com.aspose.pdf.JavascriptAction').new("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Assign JavascriptAction object to desired action of Document

doc.setOpenAction(javaScript)

# Adding JavaScript at Page Level

doc.getPages().get_Item(2).getActions().setOnOpen(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is opened')"))

doc.getPages().get_Item(2).getActions().setOnClose(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is closed')"))

# Save PDF Document

doc.save(data_dir + "JavaScript-Added.pdf")

puts "Added JavaScript Successfully, please check the output file."
```

## 
Télécharger le code d'exécution



Téléchargez**Ajout de JavaScript (Aspose.PDF)**À partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)
