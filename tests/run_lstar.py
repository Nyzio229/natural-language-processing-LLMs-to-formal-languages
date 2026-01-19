from aalpy.learning_algs import run_Lstar
from aalpy.oracles import RandomWMethodEqOracle
from sul_llm import LLMOracleSUL

ALPHABET = ['0', '1']

def main():
    sul = LLMOracleSUL()

    # Equivalence oracle — arguments MUST be positional
    eq_oracle = RandomWMethodEqOracle(
        ALPHABET,
        sul,
        1000,   # number of tests
        20     # max test length
    )

    learned_dfa = run_Lstar(
        alphabet=ALPHABET,
        sul=sul,
        eq_oracle=eq_oracle,
        automaton_type='dfa',
        print_level=2
    )

    learned_dfa.visualize("dfa_even_ones_llm")

    print("\n=== DFA learned from LLM oracle ===")
    print(f"States: {len(learned_dfa.states)}")
    print(f"Initial state: {learned_dfa.initial_state}")

    accepting = [s for s in learned_dfa.states if s.is_accepting]
    print(f"Accepting states: {accepting}")


if __name__ == "__main__":
    main()
