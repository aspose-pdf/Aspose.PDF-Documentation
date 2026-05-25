---
title: Converter PDF para PDF/A, PDF/E e PDF/X em Python
linktitle: Converter PDF para PDF/A, PDF/E e PDF/X
type: docs
weight: 120
url: /pt/python-net/convert-pdf-to-pdf_x/
lastmod: "2026-05-18"
description: Aprenda como converter arquivos PDF para PDF/A, PDF/E e PDF/X em Python com Aspose.PDF for Python via .NET para arquivamento, acessibilidade e fluxos de trabalho de impressão.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como converter PDF para formatos PDF/x
Abstract: O artigo oferece um guia abrangente sobre a conversão de PDF para os formatos PDF/A, PDF/E e PDF/X usando Aspose.PDF for Python.
---

**Formato PDF para PDF/x significa a capacidade de converter PDF para formatos adicionais, nomeadamente PDF/A, PDF/E e PDF/X.**

## Converter PDF para PDF/A

**Aspose.PDF for Python** permite que você converta um arquivo PDF para um <abbr title="Portable Document Format / A">PDF/A</abbr> arquivo PDF compatível. Antes de fazer isso, o arquivo deve ser validado. Este tópico explica como.

{{% alert color="primary" %}}

Observe que seguimos o Adobe Preflight para validar a conformidade PDF/A. Todas as ferramentas no mercado têm sua própria “representação” da conformidade PDF/A. Por favor, consulte este artigo sobre ferramentas de validação PDF/A como referência. Escolhemos os produtos Adobe para verificar como o Aspose.PDF produz arquivos PDF porque o Adobe está no centro de tudo que está conectado ao PDF.

{{% /alert %}}

Converta o arquivo usando o método Convert da classe Document. Antes de converter o PDF para um arquivo compatível com PDF/A, valide o PDF usando o método Validate. O resultado da validação é armazenado em um arquivo XML e, então, esse resultado também é passado para o método Convert. Você também pode especificar a ação para os elementos que não podem ser convertidos usando a enumeração ConvertErrorAction.

{{% alert color="success" %}}
**Tente converter PDF para PDF/A online**

Aspose.PDF for Python apresenta-lhe uma aplicação online ["PDF para PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para PDF/A com App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

O método 'document.validate()' valida se um arquivo PDF está em conformidade com o padrão PDF/A-1B (uma versão do PDF padronizada pela ISO projetada para arquivamento de longo prazo). Os resultados da validação são salvos em um arquivo de log.

### Converter PDF para PDF/A-1B

O trecho de código a seguir mostra como converter arquivos PDF para o formato PDF/A-1B:

1. Carregue o documento PDF usando 'ap.Document'.
1. Chame o método convert com os seguintes parâmetros:
    - Caminho do arquivo de log - armazena os detalhes do processo de conversão e verificações de conformidade.
    - Formato de destino - 'ap.PdfFormat.PDF_A_1B' (padrão de arquivamento).
    - Ação de erro - 'ap.ConvertErrorAction.DELETE' — remove automaticamente os elementos que impedem a conformidade.
1. Salve o arquivo PDF/A compatível convertido no caminho de saída.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA(infile, outfile):
    """Convert PDF to PDF/A-1B format."""

    document = ap.Document(infile)
    document.convert(
        outfile.replace(".pdf", "-log.xml"),
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

### Converter PDF para PDF 2.0 e PDF/A-4

Este exemplo demonstra como converter um documento PDF em formatos padronizados mais recentes: PDF 2.0 e PDF/A-4.
Ambas as conversões ajudam a garantir a conformidade com as especificações modernas e os requisitos de arquivamento.

1. Carregue o documento de entrada usando ap.Document.
1. Execute a primeira conversão para PDF 2.0 chamando document.convert com:
    - Caminho do arquivo de log para detalhes da conversão.
    - Formato de destino - 'ap.PdfFormat.V_2_0'.
    - Ação de erro - 'ap.ConvertErrorAction.DELETE' para remover elementos não conformes.
1. Execute uma segunda conversão para PDF/A-4 usando o mesmo método, garantindo que o arquivo também esteja em conformidade com os padrões de arquivamento.
1. Salve o documento resultante no caminho de saída especificado.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA4(infile, outfile):
    logfile = outfile.replace(".pdf", "_log.xml")

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)
    document.convert(logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### Converter PDF para PDF/A-3A com Arquivos Incorporados

O próximo trecho de código demonstra como incorporar arquivos externos em um PDF e, em seguida, converter o PDF para o formato PDF/A-3A, que suporta anexos e é adequado para arquivamento de longo prazo com conteúdo incorporado.

1. Carregue o PDF de entrada usando 'ap.Document'.
1. Crie um objeto 'FileSpecification' que aponta para o arquivo a ser incorporado (por exemplo, "aspose-logo.jpg") com uma descrição.
1. Adicione a especificação do arquivo à coleção 'embedded_files' do PDF.
1. Converta o documento para PDF/A-3A usando 'document.convert', especificando:
    - Caminho do arquivo de log.
    - Formato de destino - 'ap.PdfFormat.PDF_A_3A'.
    - Ação de erro - 'ap.ConvertErrorAction.DELETE' para remover elementos não conformes.
1. Salve o PDF convertido no caminho de saída.
1. Imprima uma mensagem de confirmação.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_attachment(infile, attachement_file, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    document = ap.Document(infile)

    fileSpecification = ap.FileSpecification(attachement_file, "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(
        logfile, ap.PdfFormat.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE
    )
    document.save(outfile)
```

### Converter PDF para PDF/A-1B com Substituição de Fonte

Esta função converte um PDF para o formato PDF/A-1B enquanto lida com fontes ausentes substituindo‑as por fontes disponíveis. Isso garante que o PDF convertido permaneça visualmente consistente e em conformidade com os padrões de arquivamento.

1. Carregue o PDF usando 'ap.Document'.
1. Converta o PDF para PDF/A-1B usando 'document.convert', especificando:
    - Caminho do arquivo de log.
    - Formato de destino - 'ap.PdfFormat.PDF_A_1B'.
    - Ação de erro - 'ap.ConvertErrorAction.DELETE' para remover elementos não conformes.
1. Salve o PDF convertido no caminho de saída.
1. Imprima uma mensagem de confirmação.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_replace_missing_fonts(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### Converter PDF para PDF/A-1B com Marcação automática

Esta função converte um documento PDF para o formato PDF/A-1B enquanto marca automaticamente o conteúdo para acessibilidade e consistência estrutural. A marcação automática melhora a usabilidade do documento para leitores de tela e garante uma estrutura semântica adequada.

1. Carregue o PDF usando 'ap.Document'.
1. Crie 'PdfFormatConversionOptions' especificando:
    - Caminho do arquivo de log.
    - Formato de destino - 'ap.PdfFormat.PDF_A_1B'.
    - Ação de erro - 'ap.ConvertErrorAction.DELETE' para remover elementos não conformes.
1. Configure 'AutoTaggingSettings':
    - Habilitar 'enable_auto_tagging = True'.
    - Defina 'heading_recognition_strategy = AUTO' para detectar automaticamente os cabeçalhos.
1. Atribua as configurações de autoetiquetagem às opções de conversão.
1. Converta o PDF usando 'document.convert(options)'.
1. Salve o PDF convertido no caminho de saída.
1. Imprima uma mensagem de confirmação.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_automatic_tagging(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE
    )

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = (
        ap.HeadingRecognitionStrategy.AUTO
    )

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Converter PDF para PDF/E

Este trecho de código demonstra como converter um documento PDF para o formato PDF/E-1, que é um padrão ISO voltado para documentação de engenharia e técnica. Esse formato preserva o layout preciso, gráficos e metadados exigidos nos fluxos de trabalho de engenharia.

1. Carregue o PDF de origem usando 'ap.Document'.
1. Crie 'PdfFormatConversionOptions' especificando:
    - Caminho do arquivo de log para rastrear problemas de conversão.
    - Formato de destino - 'ap.PdfFormat.PDF_E_1'.
    - Ação de erro - 'ap.ConvertErrorAction.DELETE' para remover elementos não conformes.
1. Converta o PDF usando 'document.convert(options)'.
1. Salve o PDF convertido no caminho de saída especificado.
1. Imprima uma mensagem de confirmação.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_E(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE
    )

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Converter PDF para PDF/X

O próximo trecho de código converte um documento PDF para o formato PDF/X-4, que é um padrão ISO comumente usado na indústria de impressão e publicação. O PDF/X-4 garante a precisão de cores, mantém a transparência e incorpora perfis ICC para uma saída consistente em diferentes dispositivos.

1. Carregue o PDF de origem usando 'ap.Document'.
1. Crie 'PdfFormatConversionOptions' especificando:
    - Caminho do arquivo de log.
    - Formato de destino - 'ap.PdfFormat.PDF_X_4'.
    - Ação de erro - 'ap.ConvertErrorAction.DELETE' para remover elementos não conformes.
1. Forneça o **arquivo de perfil ICC** para gerenciamento de cores via 'icc_profile_file_name'.
1. Especifique um **OutputIntent** com um identificador de condição (por exemplo, "FOGRA39") para requisitos de impressão.
1. Converta o PDF usando 'document.convert()'.
1. Salve o PDF convertido no caminho de saída especificado.
1. Imprima uma mensagem de confirmação.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_X(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE
    )

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(
        path.dirname(infile), "ISOcoated_v2_eci.icc"
    )
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Conversões relacionadas

- [Converter PDF para Word](/pdf/pt/python-net/convert-pdf-to-word/) para fluxos de trabalho de conteúdo editável após validação de padrões.
- [Converter PDF para HTML](/pdf/pt/python-net/convert-pdf-to-html/) quando sua saída de destino está pronta para a web em vez de PDF baseada em padrões.
