---
title: Gerenciar Cabeçalhos e Rodapés de PDF usando Java
linktitle: Gerenciar Cabeçalhos e Rodapés de PDF
type: docs
weight: 70
url: /pt/java/artifacts-header-footer/
description: Aprenda como adicionar e remover artefatos de cabeçalho e rodapé em documentos PDF usando Aspose.PDF for Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como Adicionar, Personalizar e Remover Cabeçalhos e Rodapés de PDF usando Java
Abstract: Este artigo explica como gerenciar artefatos de cabeçalho e rodapé em documentos PDF usando Aspose.PDF for Java. Ele aborda a criação de objetos reutilizáveis `HeaderArtifact` e `FooterArtifact` com estado de texto personalizado e alinhamento, a adição deles a uma página e a exclusão de artefatos de cabeçalho e rodapé existentes.
---
Os artefatos de cabeçalho e rodapé são elementos de paginação não‑conteúdo normalmente usados para rótulos repetidos, identificadores de página e enquadramento de layout.

## Criar um artefato de cabeçalho

Use este auxiliar quando precisar de um artefato de cabeçalho reutilizável com estilo de texto e alinhamento consistentes.

1. Criar um [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/).
1. Defina seu texto, configurações de fonte e cor de primeiro plano.
1. Configure o alinhamento horizontal e retorne o artefato.

```java
public static HeaderArtifact createHeaderArtifact(String text) {
    HeaderArtifact artifact = new HeaderArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## Criar um artefato de rodapé

Este helper cria um artefato de rodapé reutilizável com o mesmo padrão de estilo do artefato de cabeçalho.

1. Criar um [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/).
1. Defina seu texto, estado do texto e cor de primeiro plano.
1. Configure o alinhamento e retorne o artefato.

```java
public static FooterArtifact createFooterArtifact(String text) {
    FooterArtifact artifact = new FooterArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## Adicionar um artefato de cabeçalho

Use este exemplo quando uma página deve exibir um artefato de cabeçalho reutilizável.

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie o artefato de cabeçalho usando o método auxiliar.
1. Adicione o artefato à página e salve o arquivo de saída.

```java
public static void addHeaderArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HeaderArtifact header = createHeaderArtifact("Sample Header");
        document.getPages().get_Item(1).getArtifacts().add(header);
        document.save(outputFile.toString());
    }
}
```

## Adicionar um artefato de rodapé

Use este exemplo quando a página precisar exibir um artefato de rodapé com formatação reutilizável.

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie o artefato de rodapé através do método auxiliar.
1. Adicione o artefato à página e salve o arquivo de saída.

```java
public static void addFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FooterArtifact footer = createFooterArtifact("Sample Footer");
        document.getPages().get_Item(1).getArtifacts().add(footer);
        document.save(outputFile.toString());
    }
}
```

## Excluir artefatos de cabeçalho e rodapé

Use esta abordagem quando os artefatos de cabeçalho e rodapé existentes devem ser removidos da página.

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pela coleção de artefatos da página em ordem inversa.
1. Exclua artefatos de paginação cujo subtipo é cabeçalho ou rodapé, então salve o documento.

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
