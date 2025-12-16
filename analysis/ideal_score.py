def ideal_score(sac, bic_sac):
    return (abs(sac - 0.5) + abs(bic_sac - 0.5)) / 2
