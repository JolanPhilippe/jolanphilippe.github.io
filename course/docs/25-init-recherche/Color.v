Inductive color := Green | Red | Blue.

Definition next (c: color) : color :=
    match c with
    | Green => Red
    | Red => Blue
    | Blue => Green
    end.

Lemma next_cycle:
    forall (c: color), next (next (next c)) = c.
Proof.
    intros c.
    destruct c; simpl; reflexivity.
Qed.
    
