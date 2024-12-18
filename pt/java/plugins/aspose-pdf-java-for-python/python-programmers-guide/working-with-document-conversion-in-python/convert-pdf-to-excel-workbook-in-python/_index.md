---
title: Converter PDF para Planilha Excel em Python
type: docs
weight: 20
url: /pt/java/convert-pdf-to-excel-workbook-in-python/
lastmod: "2021-06-05"
---

Para converter um documento PDF em uma Planilha Excel usando **Aspose.PDF Java para Python**, simplesmente invoque o módulo **PdfToExcel**.

```python

doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# Instanciar objeto ExcelSave Option
excelsave=self.ExcelSaveOptions();

# Salvar a saída no formato XLS
doc.save(self.dataDir + "Converted_Excel.xls", excelsave);
print "Documento foi convertido com sucesso"
```

**Baixar Código em Execução**

Baixe **Converter PDF para Planilha Excel (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)