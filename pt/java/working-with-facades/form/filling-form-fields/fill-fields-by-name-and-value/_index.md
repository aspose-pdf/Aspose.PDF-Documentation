---
title: Preencher Campos por Nome e Valor
linktitle: Preencher Campos por Nome e Valor
type: docs
weight: 60
url: /pt/java/fill-fields-by-name-and-value/
description: Saiba como adaptar a API de preenchimento de campos da fachada Form em Java para atualizações dinâmicas de formulário nome-valor.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Preencher vários campos de formulário PDF a partir de pares nome-valor em Java
Abstract: O conjunto atual de exemplos em Java preenche campos individualmente com chamadas repetidas `fillField(...)`. Este artigo mostra como aplicar o mesmo padrão de API à sua própria coleção nome-valor sem inventar um recurso de fachada separado que não está presente nos exemplos do repositório.
---
O Java `FormExamples` classe preenche campos individuais diretamente:

```java
form.fillField("name", "John Doe");
form.fillField("address", "123 Main St, Anytown, USA");
form.fillField("email", "john.doe@example.com");
```

Se o seu aplicativo já possui um conjunto dinâmico de nomes de campos e valores, aplique o mesmo `fillField(...)` chamada dentro do seu próprio loop:

```java
for (Map.Entry<String, String> entry : values.entrySet()) {
    form.fillField(entry.getKey(), entry.getValue());
}
```

Este é um padrão de nível de aplicação derivado da mesma API Java usada em `FormExamples.fillTextFields(...)`; o repositório atual não inclui um método auxiliar dedicado separado para preenchimento baseado em mapa.
