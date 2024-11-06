---
title: Definir Informações do Arquivo PDF em PHP
type: docs
weight: 90
url: pt/java/set-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Definir Informações do Arquivo PDF

Para atualizar as informações do documento Pdf usando **Aspose.PDF Java para PHP**, basta invocar a classe **SetPdfFileInfo**.

Código PHP

```php

# Abra um documento pdf.
$doc = new Document($dataDir . "input1.pdf");

# Obter informações do documento
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF para java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("Informações do PDF");
$doc_info->setTitle("Definindo Informações do Documento PDF");

# salvar documento atualizado com novas informações
$doc->save($dataDir . "Updated_Information.pdf");

print "Atualizar informações do documento, por favor verifique o arquivo de saída.";

```

**Baixar Código em Execução**

Baixe **Definir Informações do Arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)