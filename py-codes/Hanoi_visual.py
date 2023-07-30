

def plot_towers(towers):
    """
    Return a plot of the towers of Hanoi.

    This uses matrix_plot.
    """
    K = max(max(l) for l in towers if l) + 1
    M = matrix(ZZ, K, 6 * K + 7)
    # first tower
    for t in range(len(towers[0])):
        j = t
        k = towers[0][t] - 1
        for l in range(K+1-k,K+2+k):
            M[K-1-j,l] = 1
    # second tower
    for t in range(len(towers[1])):
        j = t
        k = towers[1][t] - 1
        for l in range(3*K+3-k,3*K+4+k):
            M[K-1-j,l] = 1
    # third tower
    for t in range(len(towers[2])):
        j = t
        k = towers[2][t]-1
        for l in range(5*K+5-k,5*K+6+k):
            M[K-1-j,l] = 1

    return matrix_plot(M, axes=False)

def animate_towers(towers,a=0,b=1,c=2,k=-1):
    '''Move last k discs from column a into column b
    
    Assumes that the last k discs of column a are all smaller 
    than the discs in columns b and c
    '''
    if k==0:  return
    if k==-1: k=len(towers[a])
    for t in animate_towers(towers,a,c,b,k-1):
        yield t
    disc = towers[a].pop()
    towers[b].append(disc)
    yield plot_towers(towers)
    for t in animate_towers(towers,c,b,a,k-1):
        yield t

towers = (range(4,0,-1),[],[])
initial = plot_towers(towers)
frame_list=[initial]+list(animate_towers(towers))
animate(frame_list, axes=False).show(delay=80)