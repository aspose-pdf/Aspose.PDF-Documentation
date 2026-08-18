---
title: Preencher AcroForm - Preencher formulário PDF usando Java
linktitle: Preencher AcroForm
type: docs
weight: 20
url: /java/fill-form/
description: Preencha os campos do AcroForm em um documento PDF usando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Preencha campos AcroForm em arquivos PDF com Java
Abstract: Este artigo explica como preencher campos AcroForm usando Aspose.PDF para Java. O exemplo carrega um PDF por meio da fachada do Formulário, compara os nomes dos campos com um mapa de valores, atualiza os campos correspondentes e salva o documento concluído.
---
A fachada `Form` pode ser usada para automatizar o preenchimento de campos em um AcroForm existente.

## Preencha os campos do AcroForm com novos valores

1. Abra o documento PDF com a fachada [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
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
