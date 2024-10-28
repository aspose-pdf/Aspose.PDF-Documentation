---
title: Instalar com Instalador MSI
type: docs
weight: 10
url: /reportingservices/install-with-msi-installer/
lastmod: "2021-06-05"
---

Você pode instalar o Aspose.Pdf para Reporting Services usando um instalador MSI. Execute Aspose.Pdf.ReportingServices.msi e siga os passos oferecidos pelo instalador. O instalador irá copiar o assembly e outros arquivos para o diretório especificado e instalar o produto na instância padrão do Reporting Services. Você não precisa copiar ou modificar nenhum arquivo manualmente, a menos que deseje adicionar parâmetros de configuração especiais, conforme descrito na seção 'Configurar Aspose.Pdf para Reporting Services'.

A instalação automática é a melhor opção que funciona na maioria dos casos. No entanto, você pode precisar instalar o produto manualmente em algumas situações, como:

- A instalação automática falha devido a problemas de segurança de I/O.
- Você precisa instalar o produto em uma instância nomeada (não padrão) do Reporting Services 2016 ou em múltiplas instâncias.
- Você faz upgrade para a versão mais recente e deseja apenas substituir o assembly ao invés de desinstalar a versão antiga e instalar a nova usando o instalador MSI.
```
{{% alert color="primary" %}}

Nota: Observe que, no último caso, você pode acabar com outros componentes (como a documentação offline) não atualizados para a versão correspondente.

{{% /alert %}}