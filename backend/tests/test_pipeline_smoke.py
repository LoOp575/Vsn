from app.pipeline.formula_pipeline import FormulaPipeline


def test_pipeline_instance():
    pipeline = FormulaPipeline()
    assert pipeline is not None
    assert hasattr(pipeline, 'run')
