---
title: Converter PDF para o Formato SVG em Python
type: docs
weight: 30
url: pt/java/convert-pdf-to-svg-format-in-python/
lastmod: "2021-06-05"
---

Para converter PDF para o formato SVG usando **Aspose.PDF Java para Python**, basta invocar o módulo **PdfToSvg**.

```python

# Abra o documento alvo
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# instanciar um objeto de SvgSaveOptions
save_options = self.SvgSaveOptions()

# não comprimir a imagem SVG para o arquivo Zip
save_options.CompressOutputToZipArchive = False;

# Salvar a saída no formato XLS
doc.save(self.dataDir + "Output1.svg", save_options)

print "Documento foi convertido com sucesso"
```

**Baixar Código em Execução**

Baixe **Converter PDF para o Formato SVG (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)