---
title: Obter Informações do Arquivo PDF em PHP
type: docs
weight: 40
url: /pt/java/get-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obter Informações do Arquivo PDF

Para obter informações do arquivo de documento PDF usando **Aspose.PDF Java para PHP**, basta invocar a classe **GetPdfFileInfo**.

Código PHP

```php

# Abrir um documento PDF.
$doc = new Document($dataDir . "input1.pdf");

# Obter informações do documento
$doc_info = $doc->getInfo();

# Mostrar informações do documento
print "Autor:-" . $doc_info->getAuthor();
print "Data de Criação:-" . $doc_info->getCreationDate();
print "Palavras-chave:-" . $doc_info->getKeywords();
print "Data de Modificação:-" . $doc_info->getModDate();
print "Assunto:-" . $doc_info->getSubject();
print "Título:-" . $doc_info->getTitle();

```

**Baixar Código em Execução**

Baixar **Obter Informações do Arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)