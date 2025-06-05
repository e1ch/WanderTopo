// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:wander_topo/main.dart';

void main() {
  testWidgets('App should render correctly', (WidgetTester tester) async {
    await tester.pumpWidget(const WanderTopoApp());

    // Verify that the app title is displayed
    expect(find.text('WanderTopo'), findsOneWidget);

    // Verify that the welcome message is displayed
    expect(find.text('Welcome to WanderTopo'), findsOneWidget);

    // Verify that the explore button is displayed
    expect(find.text('Explore'), findsOneWidget);

    // Verify that the plan button is displayed
    expect(find.text('Plan'), findsOneWidget);
  });
}
