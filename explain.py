import shap

def explain_prediction(model, input_df, feature_cols):
    explainer = shap.TreeExplainer(model)
    shap_vals = explainer.shap_values(input_df[feature_cols])[0]
    impacts = sorted(zip(feature_cols, shap_vals), key=lambda x: abs(x[1]), reverse=True)[:5]
    return [{"feature": f, "impact": round(float(v), 3)} for f, v in impacts]