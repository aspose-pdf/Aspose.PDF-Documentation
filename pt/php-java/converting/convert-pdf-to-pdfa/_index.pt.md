---
title: Converter PDF para formatos PDF/A 
linktitle: Converter PDF para formatos PDF/A 
type: docs
weight: 100
url: /php-java/convert-pdf-to-pdfa/
lastmod: "2024-05-20"
description: Este tópico mostra como o Aspose.PDF permite converter um arquivo PDF em um arquivo PDF compatível com PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF para PHP** permite converter um arquivo PDF em um arquivo PDF compatível com PDF/A. Antes de fazer isso, o arquivo deve ser validado. Este artigo explica como.

Por favor, note que seguimos o Adobe Preflight para validar a conformidade com PDF/A. Todas as ferramentas no mercado têm sua própria "representação" da conformidade com PDF/A. Por favor, verifique este artigo sobre [ferramentas de validação PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) para referência. Escolhemos produtos da Adobe para verificar como o Aspose.PDF produz arquivos PDF porque a Adobe está no centro de tudo que está conectado ao PDF.

Antes de converter o PDF para um arquivo compatível com PDF/A, valide o PDF usando o método de validação.
 O resultado da validação é armazenado em um arquivo XML e, em seguida, este resultado também é passado para o método de conversão. Você também pode especificar a ação para os elementos que não podem ser convertidos usando a enumeração [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

## Conversão de PDF para PDF/A

O trecho de código a seguir mostra como converter arquivos PDF para PDF compatível com PDF/A-1b.

```php
// Crie um novo objeto Document e carregue o arquivo PDF de entrada.
$documento = new Document($inputFile);

// Converta o documento para o formato PDF/A-1a e especifique o arquivo de log e a ação de erro.
$res = $documento->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// Salve o documento convertido no arquivo de saída.
$documento->save($outputFile);
```

Para realizar apenas a validação, use a seguinte linha de código:

```php
// Crie um novo objeto Document e carregue o arquivo PDF de entrada.
$documento = new Document($inputFile);

// Converta o documento para o formato PDF/A-1a e especifique o arquivo de log e a ação de erro.
$res = $documento->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// Validar PDF para PDF/A-1a
if ($documento->validate("validation-result-A1A.xml", PdfFormat.PDF_A_1A))
{
    echo "Válido";
}
else
{
    echo "Não válido";
}
```

{{% alert color="primary" %}}
**Tente converter PDF para PDF/A online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["PDF para PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF PDF para PDF/A com Aplicativo Gratuito](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}