funcionario = "João Silva"
salario_bruto = 3500.00
percentual_inss = 0.11

desconto_inss = salario_bruto * percentual_inss
salario_liquido = salario_bruto - desconto_inss

print("===============")
print("HOLERITE - MÊS 02/2026")
print("===============")
print("Funcionário:", funcionario)

print(f"Salário bruto: R$ {salario_bruto:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print(f"Desconto INSS: R$ {desconto_inss:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print(f"Salário líquido: R$ {salario_liquido:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
