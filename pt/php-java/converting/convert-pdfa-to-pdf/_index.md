---
title: Converter PDF/A para formato PDF 
linktitle: Converter PDF/A para formato PDF
type: docs
weight: 110
url: pt/php-java/convert-pdfa-to-pdf/
lastmod: "2024-05-20"
description: Este tópico mostra como o Aspose.PDF permite converter arquivo PDF/A para documento PDF com biblioteca PHP. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Converter documento PDF/A para PDF

Converter documento PDF/A para PDF significa remover a restrição de <abbr title="Portable Document Format Archive">PDF/A</abbr> do documento original. A classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) possui o método removePdfaCompliance(..) para remover
as informações de conformidade PDF do arquivo de entrada/origem.

```php
// Criar uma nova instância da classe Document com o arquivo de entrada
$document = new Document($inputFile);

// Remover a conformidade PDF/A do documento
$document->removePdfaCompliance();

// Salvar o documento modificado no arquivo de saída
$document->save($outputFile);
```

Esta informação também é removida se você fizer quaisquer alterações no documento (por exemplo.
 add pages). No exemplo a seguir, o documento de saída perde a conformidade com PDF/A após a adição da página.

```php
// Crie uma nova instância da classe Document com o arquivo de entrada
$document = new Document($inputFile);

// Remova a conformidade com PDF/A do documento
$document->getPages()->add();

// Salve o documento modificado no arquivo de saída
$document->save($outputFile);
```