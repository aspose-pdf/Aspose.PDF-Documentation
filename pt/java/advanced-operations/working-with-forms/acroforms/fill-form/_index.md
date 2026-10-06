---
title: Preencher AcroForm - preencher formulário PDF usando Java
linktitle: Preencher AcroForm
type: docs
weight: 20
url: /pt/java/fill-form/
description: Preencher campos AcroForm em um documento PDF usando Aspose.PDF for Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Preencher campos AcroForm em arquivos PDF com Java
Abstract: Este artigo explica como preencher campos AcroForm usando Aspose.PDF for Java. O exemplo carrega um PDF através da fachada Form, compara os nomes dos campos com um mapa de valores, atualiza os campos correspondentes e salva o documento concluído.
---
O `Form` facade pode ser usado para automatizar o preenchimento de campos em um AcroForm existente.

## Preencher os campos AcroForm com novos valores

1. Abra o documento de formulário PDF com a fachada [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Itere pelos campos do formulário e atualize as entradas correspondentes com os valores fornecidos.
1. Salve o documento PDF atualizado.

```java
public static void fillForm(Path inputFile, Path outputFile) {
    Map<String, String> newFieldValues = Map.of(
            "First Name", "Alexander_New",
            "Last Name", "Greenfield_New",
            "City", "Yellowtown_New",
            "Country", "Redland_New");

    Form form = new Form(inputFile.toString());
    try {
        for (String fieldName : form.getFieldNames()) {
            if (newFieldValues.containsKey(fieldName)) {
                form.fillField(fieldName, newFieldValues.get(fieldName));
            }
        }
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
