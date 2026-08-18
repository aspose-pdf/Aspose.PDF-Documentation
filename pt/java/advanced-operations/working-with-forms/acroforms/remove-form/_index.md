---
title: Excluir formulários de PDF em Java
linktitle: Excluir formulários
type: docs
weight: 70
url: /java/remove-form/
description: Remova objetos de formulário de páginas PDF usando Aspose.PDF para Java, incluindo limpeza completa e exclusão direcionada.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remova recursos de formulário de páginas PDF com Java
Abstract: Este artigo explica como remover recursos de formulário de documentos PDF usando Aspose.PDF para Java. Abrange a limpeza de todos os formulários de uma página e a exclusão apenas dos recursos selecionados do formulário da máquina de escrever após filtrar a coleção de formulários da página.
---
Esses exemplos removem recursos de formulário de uma página em vez de apenas alterar os valores dos campos.

## Remover todos os recursos de formulário de uma página

Use este exemplo quando todos os recursos de formulário em uma página selecionada precisarem ser removidos em uma operação.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) da página de destino.
1. Limpe a coleção e salve o documento atualizado.

```java
public static void removeAllForms(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        forms.clear();
        document.save(outputFile.toString());
    }
}
```

## Remover recursos específicos do formulário

Use este exemplo quando apenas recursos de formulário selecionados, como formulários de máquina de escrever, devem ser excluídos.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) da página de destino.
1. Filtre os recursos [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) que deseja remover e exclua-os da coleção.
1. Salve o [documento] PDF atualizado (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void removeSpecifiedForm(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        List<String> formNames = new ArrayList<>();
        for (XForm form : forms) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                formNames.add(forms.getFormName(form));
            }
        }
        for (String formName : formNames) {
            forms.delete(formName);
        }
        document.save(outputFile.toString());
    }
}
```
