---
title: Limitações da API
type: docs
weight: 70
url: pt/net/api-limitations/
---

## **Xsl Fo para Pdf**
A seguir estão os problemas conhecidos do suporte XSL-FO.

- SVG não é suportado
## **Informações do criador do PDF**
- Observe que você não pode definir valores para os campos **Application** e **Producer**, porque Aspose Ltd. e Aspose.PDF para .NET x.x.x serão exibidos nesses campos
## **Outros**
A seguir estão alguns outros problemas conhecidos.

- Pdf/X não é suportado.
- Formulário XFA dinâmico não é suportado: Como suas páginas são criadas/renderizadas no momento do carregamento do PDF, no Adobe Acrobat/Reader. Assim, não podemos extrair e salvar nenhuma dessas páginas virtuais ou várias páginas. Em vez disso, nós (e o Adobe Acrobat) podemos extrair apenas uma verdadeira página que contém apenas mensagem de erro.
- Os símbolos especiais $p e $P não funcionarão se não terminarem com um caractere em branco.
- Conversão de HTML para PDF: HTML é uma linguagem muito vasta e com cada novo lançamento do Aspose.PDF para .NET, fazemos o nosso melhor para entregar uma versão melhor e mais robusta da conversão de HTML para PDF (*suportando todos os tipos de HTML*), mas como existem inúmeros arquivos HTML com diferentes naturezas/estruturas e complexidades, às vezes nosso componente encontra alguns problemas em termos de formatação ao renderizar conteúdos HTML para o formato PDF e isso geralmente acontece ao usar documentos com estruturas complexas.
- Conversão de HTML para PDF: HTML é uma linguagem muito vasta e com cada novo lançamento do Aspose.PDF para .NET, tentamos fazer o nosso melhor para entregar uma versão mais robusta da conversão de HTML para PDF (*ao suportar todos os tipos de HTML*), mas como existem numerosos arquivos HTML com diferentes naturezas/estruturas e complexidades, às vezes nosso componente encontra alguns problemas em termos de formatação ao renderizar conteúdos HTML para o formato PDF e isso geralmente acontece ao usar documentos com estruturas complexas.
- A incorporação de fontes não é suportada no MS Word para Macintosh e também observe que no MS Word para Windows, ela é limitada apenas a fontes TrueType. Portanto, ao visualizar arquivos word(DOC) gerados como resultado da conversão de PDF para DOC através do Aspose.PDF para .NET, as fontes incorporadas são substituídas ao visualizar os arquivos no MS Word no MAC OS. Para mais detalhes, por favor, consulte [macsupportcentral](http://www.macsupportcentral.com/2012/05/embed-fonts-microsoft-office-word-files/).
