def rule(n, t, s):
    g=["0"*t+s+"0"*t]
    for i in range(t):g+=[(" "*(i+1)+"".join([f"{n:08b}"[::-1][int(g[i].strip()[j-2:j+1],2)]for j in range(2,len(g[0])-2*i)])+" "*(i+1))]
    return"\n".join([r"\begin{tabular}{ "+"c "*len(g[0])+"}",*[fr"{' & '.join(c)} \\" for c in g],r"\end{tabular}"])


def rec_rule(n,t,s):
    r=lambda g,t,i:["  & "*i+" & ".join(g)+" &  "*i+r" \\"]+(r("".join([f"{n:08b}"[::-1][int(g[j-2:j+1],2)]for j in range(2,len(g))]),t-1,i+1)if t>0 else[r"\end{tabular}"])
    return"\n".join([r"\begin{tabular}{ "+"c "*(len(s)+2*t)+"}"]+r("0"*t+s+"0"*t,t,0))


def rule_no_tex(n, t, seed):
    r=lambda x,t:["".join(x)]+(r("".join([f"{n:b}".zfill(8)[::-1][int(x[j-2:j+1],2)]for j in range(2,len(x))]),t-1)if t>0else[])
    return r("0"*t+seed+"0"*t,t)


def rule_no_code_golf(n: int, t: int, seed: str) -> str:
    seed = "0" * t + seed + "0" * t
    rule = f"{n:b}".zfill(8)[::-1]
    gens = [seed]

    out = f"\\begin{{tabular}}{{ {'c ' * len(seed)} }}\n"
    for i in range(t):
        prev_gen = gens[i]
        new_gen = []
        for j in range(1, len(prev_gen) - 1):
            new_gen.append(rule[int(prev_gen[j-1:j+2], 2)])

        new_gen = "".join(new_gen)
        gens.append(new_gen)

    for i, gen in enumerate(gens):
        out += " &  " * i + f"{' & '.join(gen)}" + " &  " * i + "\\\\\n"

    out += "\\end{tabular}"
    return out


print(rule_no_tex(110, 3, "00101101001"))
