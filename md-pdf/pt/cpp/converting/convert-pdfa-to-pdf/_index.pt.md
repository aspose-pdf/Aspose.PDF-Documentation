---
title: Converter PDF/A para formato PDF 
linktitle: Converter PDF/A para formato PDF
type: docs
weight: 110
url: /cpp/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: Este tópico mostra como Aspose.PDF permite converter um arquivo PDF/A para documento PDF com a biblioteca C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Converter documento PDF/A para PDF

Converter documento PDF/A para PDF significa remover a restrição <abbr title="Portable Document Format Archive
">PDF/A</abbr> do documento original. A classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) tem o método 'RemovePdfaCompliance' para remover as informações de conformidade PDF do arquivo de entrada/origem.
Após [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) o arquivo de entrada.

```cpp
void ConvertPDFAtoPDF()
{
    std::clog << "PDF/A para PDF conversão: Início" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);

    // Remover informações de conformidade PDF/A
    document->RemovePdfaCompliance();

    // Salvar documento atualizado
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A para PDF conversão: Fim" << std::endl;
}
```

Esta informação também é removida se você fizer quaisquer alterações no documento (por exemplo, adicionar páginas). No exemplo a seguir, o documento de saída perde a conformidade com o PDF/A após a adição de páginas.

```cpp
void ConvertPDFAtoPDFAdvanced()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    // Adicionar uma nova página (vazia) remove as informações de conformidade PDF/A.

    document->get_Pages()->Add();
    // Salvar documento atualizado
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```