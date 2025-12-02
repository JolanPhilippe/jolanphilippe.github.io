(* Sujet *)

Section Exercices.

  (* (A ∧ B) → (B ∧ A) *)
  Lemma permutation: forall (A B: Prop), A /\ B -> B /\ A.
  Proof.
    intros A B h. 
    destruct h as [ha hb]. 
    split; assumption.
  Qed.

  (* (A ∧ B) ∧ C → A ∧ (B ∧ C)) *)
  Lemma association: forall (A B C: Prop), (A /\ B) /\ C -> A /\ (B /\ C).
  Proof.
    intros A B C h. 
    destruct h as [hab hc]. 
    destruct hab as [ha hb].
    split; [assumption | split; assumption].
  Qed.

  (* (A ∧ B) → A *)
  Lemma elimination: forall (A B: Prop), A /\ B -> A.
  Proof.
    intros A B h.
    destruct h as [ha hb]. 
    assumption.
  Qed.

  (* (A → (B ∧ C)) → (A → B) *)
  Lemma distribution: forall (A B C: Prop), (A -> (B /\ C)) -> (A -> B).
  Proof.
    intros A B C h a0. apply (proj1 (h a0))
  Qed.

  (* A → (A ∨ C) *)
  Lemma disjonction1: forall (A B C: Prop), A -> (A \/ C).
  Proof.
    intros A B C a.
    left; assumption.
  Qed.

  (* B → (A ∨ B) *)
  Lemma disjonction2: forall (A B C: Prop), B -> (A \/ B).
  Proof.
    intros A B C a.
    right; assumption.
  Qed.

  (*  (A ∧ B → C) → A → B → C *)
  Lemma currying: forall (A B C: Prop), (A /\ B -> C) -> A -> B -> C.
  Proof.
    intros A B C h ha hb.
    apply h. split. 
    - assumption.
    - assumption.
  Qed.

  (* (A → B → C) → (A ∧ B) → C *)
  Lemma uncurrying: forall (A B C: Prop), (A -> B -> C) -> (A /\ B) -> C.
  Proof.
    intros A B C h hab. 
    destruct hab as [ha hb]. 
    apply h; assumption.
  Qed.

  (* (A → C) → (B → C) → (A ∨ B) → C *) 
  Lemma rais_par_cas: forall (A B C: Prop), (A -> C) -> (B -> C) -> (A \/ B) -> C.
  Proof.
    intros A B C Hac Hbc Hab.
    destruct Hab.
    - apply Hac. assumption.
    - apply Hbc. assumption.
  Qed.

End Exercices.
