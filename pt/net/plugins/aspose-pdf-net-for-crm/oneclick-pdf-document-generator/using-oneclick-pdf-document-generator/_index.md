---
title: Usando o Gerador de Documentos PDF OneClick
type: docs
weight: 10
url: pt/net/using-oneclick-pdf-document-generator/
description: Aprenda a usar o Gerador de Documentos PDF OneClick da Aspose.PDF no Microsoft Dynamics
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Criar Modelo e Adicionar no CRM

- Abra o word e crie um modelo.
- Insira campos MailMerge para dados vindos do CRM.

![Inserir campos MailMerge](using-oneclick-pdf-document-generator_1.png)

- Certifique-se de que o nome do campo corresponda exatamente com o campo do CRM.
- Os modelos são específicos para uso com entidade individual.

![Modelo Demonstrativo](using-oneclick-pdf-document-generator_2.png)

- Uma vez que o modelo esteja criado, abra a entidade de Configuração do PDF OneClick no CRM e Crie um Novo registro.
- Dê o nome do modelo, selecione a entidade para a qual o modelo é definido e anexe o documento criado no anexo.

![Selecionar Modelo](using-oneclick-pdf-document-generator_3.png)

## Gerar Documento a partir do Botão na Faixa de Opções

- Abra o Registro onde você deseja gerar o documento.
- Abra o Registro onde você deseja gerar o documento.
- Clique no botão OneClick PDF na faixa de opções.

![Clique no OneClick PDF](using-oneclick-pdf-document-generator_4.png)

- No Popup: Selecione o modelo, Nome do Arquivo e Ação e Clique em Gerar.
- Verifique o arquivo baixado ou Notas, com base na seleção.

## Configure os Botões OneClick e use-os

- Para usar o Botão OneClick diretamente do Formulário, abra a Personalização do Formulário.
- Insira WebResource onde você deseja adicionar Botões OneClick.
- Selecione OpenButtonPage no Webresource e dê um Nome.
- Configure os Botões no campo de Dados no seguinte exemplo.

![Propriedades do WebResource](using-oneclick-pdf-document-generator_5.png)

- Use uma linha separada para cada botão e use a seguinte sintaxe:
  - Sintaxe: Nome do Modelo |<Ação: Baixar/Nota>|Nome do Arquivo de Saída
  - Exemplo: Demo|Baixar|Meu Arquivo Baixado
- Salve e publique a personalização.
- O botão está disponível no formulário.

![O botão está disponível no formulário](using-oneclick-pdf-document-generator_6.png)
![O botão está disponível no formulário](using-oneclick-pdf-document-generator_6.png)
