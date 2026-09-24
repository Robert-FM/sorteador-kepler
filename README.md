# 🎲 Sorteador Kepler

Aplicação desktop em Python para sortear um número inteiro entre dois limites definidos pelo usuário. A interface utiliza Tkinter e ttk, com campos de entrada, botões para sortear e limpar e resultado em destaque.

## ✨ Funcionalidades

- Sorteio entre limites inclusivos: o mínimo e o máximo podem ser sorteados.
- Campos inicialmente vazios, com a dica visual **Digite um inteiro**.
- Validação de entradas vazias, textos e valores que não representam números inteiros.
- Mensagem de erro quando o mínimo é maior que o máximo.
- Novo sorteio pelo botão **Sortear número** ou pela tecla **Enter**.
- Botão **Limpar**, ao lado de **Sortear número**, para apagar os dois limites e restaurar o resultado e a mensagem inicial.
- Botões compactos e centralizados abaixo dos campos: **Sortear número** em azul e **Limpar** com fundo cinza claro e borda preta para facilitar a identificação.
- Os botões mudam de cor ao passar o mouse e clicar; a borda preta de **Limpar** permanece visível.
- Janela de 600 × 480 pixels, centralizada na tela, com painel centralizado.

O sorteio utiliza `random.randint`. Cada execução é independente e pode repetir números anteriores. Valores negativos são aceitos; limites iguais sempre produzem aquele valor. Não há histórico nem armazenamento dos resultados.

## 🛠️ Tecnologias

- **Python:** lógica e execução da aplicação.
- **Tkinter e ttk:** janela, componentes e estilos da interface.
- **random:** geração do número pseudoaleatório.

Não há dependências externas de execução declaradas. O `uv_build` aparece no `pyproject.toml` como ferramenta de construção do pacote, não como biblioteca necessária para executar `main.py`.

## 📁 Organização

```text
sorteador/
├── .gitignore
├── .python-version
├── interface.py
├── main.py
├── pyproject.toml
├── sorteador.py
└── README.md
```

`main.py` chama `iniciar_interface()`, definida em `interface.py`. A classe `InterfaceSorteador` organiza a configuração da janela, os estilos, os componentes e as ações do usuário. Ao sortear, ela converte as entradas em inteiros e chama `sorteador(num_a, num_b)`, em `sorteador.py`, que valida a ordem dos limites e devolve o número.

## ▶️ Preparação e execução

É necessário ter **Python 3.14 ou superior**, conforme o `pyproject.toml`; o arquivo `.python-version` indica 3.14. O interpretador deve ter suporte a **Tkinter/Tcl/Tk**, e a execução requer uma sessão gráfica.

### Windows (PowerShell ou Prompt de Comando)

Se ainda não tiver Python, instale o **Python Install Manager** seguindo a [documentação oficial para Windows](https://docs.python.org/3.14/using/windows.html). Com esse gerenciador instalado, abra um terminal e instale o Python 3.14:

```powershell
py install 3.14
```

Se já tiver Python 3.14 instalado, pule essa instalação. Clone ou baixe e extraia o repositório, depois abra o terminal na pasta que contém `main.py`.

Confira a versão e o suporte ao Tkinter:

```powershell
py -3.14 --version
py -3.14 -m tkinter
```

O segundo comando abre uma janela de demonstração. Feche-a e execute:

```powershell
py -3.14 main.py
```

Se `py` não for reconhecido, tente `python --version` e, caso indique Python 3.14 ou superior, use `python -m tkinter` e `python main.py`. Se nenhum comando funcionar, consulte a seção de solução de problemas da documentação oficial acima.

O Tkinter acompanha as distribuições binárias oficiais do Python. Se estiver ausente na sua instalação, utilize uma distribuição com suporte a Tcl/Tk; não é necessário instalar `tkinter` com `pip`. Veja a [documentação do Tkinter](https://docs.python.org/3.14/library/tkinter.html).

### Linux/macOS (terminal)

1. Clone ou baixe este repositório e abra um terminal na pasta que contém `main.py`.
2. Confira a versão do interpretador:

   ```bash
   python3 --version
   ```

3. Confira o suporte ao Tkinter:

   ```bash
   python3 -m tkinter
   ```

   Esse comando deve abrir uma janela de demonstração. Feche-a para continuar. Se o módulo não estiver disponível, instale o suporte a Tkinter correspondente ao seu Python pelo instalador ou gerenciador de pacotes do sistema.

4. Inicie o sorteador:

   ```bash
   python3 main.py
   ```

Se o interpretador estiver disponível como `python`, utilize esse nome nos comandos, conferindo a mesma versão exigida. Não é necessário instalar pacotes com `pip` ou criar um ambiente virtual para essa execução direta.

### Configuração de empacotamento

O comando `sorteador` declarado no `pyproject.toml` aponta para `sorteador:main`, que não inicia esta interface. O pacote de exemplo local em `src` está ignorado pelo Git, e os módulos da aplicação ficam na raiz. Por isso, o caminho documentado para abrir a aplicação é `python3 main.py`; a configuração de empacotamento precisa ser ajustada antes de distribuir a interface como pacote instalável.

## 💻 Como utilizar

1. Preencha **Limite mínimo** e **Limite máximo**. Os campos começam vazios, com a dica **Digite um inteiro**.
2. Clique em **Sortear número** ou pressione **Enter**.
3. Leia o número exibido no painel.
4. Clique novamente para outro sorteio ou altere os limites antes de continuar.
5. Para começar de novo, clique em **Limpar**. Os dois campos ficam vazios, o resultado volta a **—** e a mensagem passa a ser **Escolha os limites e clique em Sortear.**

O placeholder **Digite um inteiro** é apenas uma dica visual, não um valor preenchido. Ele desaparece quando o campo recebe foco e reaparece ao sair do campo se ele continuar vazio. É necessário informar os dois limites para sortear.

Por exemplo, com mínimo `1` e máximo `5`, o resultado será um dos números `1`, `2`, `3`, `4` ou `5`. Com ambos os limites em `3`, o resultado será sempre `3`.

Em caso de entrada inválida, a interface mostra uma mensagem e substitui o resultado por um traço. Corrija os campos e tente novamente.

## ✅ Verificação manual

O projeto não possui uma suíte de testes automatizados. Os cenários abaixo descrevem o comportamento previsto pelo código e servem como roteiro de conferência manual, não como registro de testes executados em Windows, Linux ou macOS.

| Entrada ou ação | Comportamento esperado |
| --- | --- |
| Abrir a aplicação | Campos sem valores numéricos preenchidos |
| Observar os botões abaixo dos campos | Botões compactos e centralizados, com **Sortear número** azul e **Limpar** cinza claro com borda preta |
| Passar o mouse e clicar em **Limpar** | O fundo muda de cor e a borda preta permanece visível |
| Selecionar um campo vazio | Oculta a dica visual desse campo |
| Sair de um campo vazio | Mostra novamente a dica **Digite um inteiro** |
| Mínimo `1`, máximo `5` | Exibe um inteiro de 1 a 5 |
| Mínimo `3`, máximo `3` | Exibe 3 |
| Mínimo `5`, máximo `1` | Informa que o mínimo não pode superar o máximo |
| Campo vazio, `abc` ou `2.5` | Solicita números inteiros |
| Pressionar Enter com limites válidos | Realiza um sorteio |
| Clicar em **Limpar** após digitar limites ou sortear | Apaga os dois campos, substitui o resultado por **—** e restaura a mensagem inicial |
| Clicar em **Limpar** após uma entrada inválida | Apaga os dois campos e restaura a mensagem inicial |

## 👨‍💻 Autor

**Robert Melo**

🔗 LinkedIn: [linkedin.com/in/robertdemelo](https://www.linkedin.com/in/robertdemelo/)

🐍 Python | Tkinter | ttk | Interfaces gráficas desktop
